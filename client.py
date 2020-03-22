import json
import requests
import numpy as np

######### DO NOT CHANGE ANYTHING IN THIS FILE ##################
API_ENDPOINT = 'http://10.4.21.147'
PORT = 3000
MAX_DEG = 11

#### functions that you can call
def get_errors(id, vector):
    """
    returns python array of length 2 
    (train error and validation error)
    """
    for i in vector: assert -10<=abs(i)<=10
    assert len(vector) == MAX_DEG

    return json.loads(send_request(id, vector, 'geterrors'))

def submit(id, vector):
    """
    used to make official submission of your weight vector
    returns string "successfully submitted" if properly submitted.
    """
    for i in vector: assert -10<=abs(i)<=10
    assert len(vector) == MAX_DEG
    return send_request(id, vector, 'submit')

#### utility functions
def urljoin(root, port, path=''):
    root = root + ':' + str(port)
    if path: root = '/'.join([root.rstrip('/'), path.rstrip('/')])
    return root

def send_request(id, vector, path):
    api = urljoin(API_ENDPOINT, PORT, path)
    vector = json.dumps(vector)
    response = requests.post(api, data={'id':id, 'vector':vector}).text
    if "reported" in response:
        print(response)
        exit()

    return response


if __name__ == "__main__":
    """
    Replace "test" with your secret ID and just run this file 
    to verify that the server is working for your ID.
    """
    print("running")
    err = get_errors('jOZFaYXSYOb7jnBxC3u7F66X1uRy6oOvLnWyHc1TQeu7zhCSB4', [-7.810503810575697425e-01,2.249750646858881542e-01,-6.823840839346558163e+00,-6.635547926274353303e-01,-7.561125745275590337e-02,1.860489450620816665e-01,-9.606348351822812104e-01,-6.750149915342297247e-01,5.377553912974620820e-01,9.570554538540849698e-01,4.328127847805320894e-01])
    assert len(err) == 2
    print("finished error request")
    print(err, err[1])

    print( "running" )
    err = get_errors( 'jOZFaYXSYOb7jnBxC3u7F66X1uRy6oOvLnWyHc1TQeu7zhCSB4',
                      [6.807785660514034110e-01,6.053076917263464640e-01,-5.379694936573812925e+00,5.365491358890800422e-01,-4.569004977576232029e-01,-8.970144317105099852e-01,-4.293032136916184460e-01,-7.051820362819628818e-02,-1.804532752574311005e-01,-1.699647031586449739e-02,1.341636315976826033e-01] )
    assert len( err ) == 2
    print( "finished error request" )
    print( err, err[1]  )

    # submit_status = submit('test', list(-np.arange(0,1.1,0.1)))
    # assert "submitted" in submit_status
    
