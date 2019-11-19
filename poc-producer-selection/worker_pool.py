import hashlib as hash 
import random


def setup_worker_lists(no_worker, prev_ledg_update):
    """
    Generates the list of workers and their coresponding information (Random no. and fees paid
    """
    
    list_of_workers = []

    for PiD in range(no_worker):
        work_info_list = worker_info(PiD, prev_ledg_update)
        list_of_workers.append(work_info_list)

    return list_of_workers


def worker_info(PiD, last_ledger_value):

    """
    This generates the worker list, this includes 4 elements:
    - PID, this will be a number between 0 and the number of selected workers in the worker pool 
    - rand_no, this is the random number that is associated with the worker this is an int generated 
      from a hash of the user selected random int and the int of the hash of the previous ledger cycle
    - personal_rand, is the user selected random int
    - fee_paid, is a bool as to whether the fee has been paid 
    """
    work_info_list = []
    fee_paid = worker_pay_fee()
    personal_rand = random.randint(1,2**512)
    combined_rand = bytes(str((personal_rand + last_ledger_value) % 2**512),'utf-8') 
    rand_no = gen_rand_no(combined_rand)
    work_info_list.append(PiD)
    work_info_list.append(rand_no)
    work_info_list.append(personal_rand)
    work_info_list.append(fee_paid)

    return (work_info_list)


def gen_rand_no(combined_rand):

    """
    This function generates a randomised number after hashing an input. 
    """

    rand_no = hash.blake2b()
    rand_no.update(combined_rand)
    rand_no = rand_no.hexdigest()
    rand_no = int(rand_no, base=16)

    return (rand_no)


def worker_pay_fee():
    """
        This randomises some worker nodes to not having paid fees
    """
    odds = random.randint(0,9)

    if odds == 1:

        return False

    else:

        return True