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
    err = get_errors( 'jOZFaYXSYOb7jnBxC3u7F66X1uRy6oOvLnWyHc1TQeu7zhCSB4',
                      [0.000000000000000000e+00, 2.958001952514397945e-02, -9.008730089066498137e-02,
                       3.708721824285533125e-02, -2.269800158022661985e-05, 9.282235081380621861e-12,
                       1.878061102895531119e-10, -3.965997477030931685e-13, -1.722820070429421772e-13,
                       1.747185773416640936e-12, 4.199810469868679031e-16] )
    assert len( err ) == 2
    print( "finished error request" )
    print( err, err[1] + err[0], err[1] + 0.5 * err[0] )

    # print( "running" )
    # err = get_errors( 'jOZFaYXSYOb7jnBxC3u7F66X1uRy6oOvLnWyHc1TQeu7zhCSB4',
    #                   [6.807785660514034110e-01,6.053076917263464640e-01,-5.379694936573812925e+00,5.365491358890800422e-01,-4.569004977576232029e-01,-8.970144317105099852e-01,-4.293032136916184460e-01,-7.051820362819628818e-02,-1.804532752574311005e-01,-1.699647031586449739e-02,1.341636315976826033e-01] )
    # assert len( err ) == 2
    # print( "finished error request" )
    # print( err, err[1]  )

    # submit_status = submit('test', list(-np.arange(0,1.1,0.1)))
    # assert "submitted" in submit_status
    
