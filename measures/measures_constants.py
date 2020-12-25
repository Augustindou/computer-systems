# juste pour dire
import numpy as np

VERBOSE = True

# paths to directories
root_path = "../"
java_project_path = f"{root_path}computer-systems/"
exec_path = f"{root_path}java_executables/"
input_path = f"{root_path}regex-generation/"
output_path = f"{root_path}output_files/"
src_path = f"{java_project_path}src/"
plt_path = f"{root_path}plots/"

# number of clients
n_clients = [40, 2, 5, 10, 20, 30, 50, 75, 100]
# delay [ms]
delays = np.array([10, 2, 4, 6, 8, 15, 20, 30, 40, 50])*1000
# server threads
n_threads = [6, 2, 4, 8, 10, 12, 16]

# input files (txt and path will be added), will always run all inputs
input_files = ["easy-requests-100", "hard-requests-100", "network-intensive-requests-100"]
# for testing
n_clients = [40, 2]
delays = np.array([1, 2])*1000
n_threads = [6, 2]
input_files = ["easy-requests-100", "network-intensive-requests-100"]

# code variables
hostname = "::1"
port     = 10069
db_file  = f"{java_project_path}assets/dbdata.txt"
verbose_clients = "false"

variable_inputs = np.array([(n_clients[0], delays[0], n_threads[0])])
for n in n_clients[1:] : variable_inputs = np.append(variable_inputs, [(n           , delays[0], n_threads[0])], axis=0)
for d in delays   [1:] : variable_inputs = np.append(variable_inputs, [(n_clients[0], d        , n_threads[0])], axis=0)
for t in n_threads[1:] : variable_inputs = np.append(variable_inputs, [(n_clients[0], delays[0], t           )], axis=0)

client_output_file = lambda f, n, d, t : f"{output_path}CLIENT_{f}_{n}clients_{d}delay_{t}threads"
server_output_file = lambda f, n, d, t : f"{output_path}SERVER_{f}_{n}clients_{d}delay_{t}threads"