import gmpy2
import random
import assets
import Alice
import Bob
import time

def main():
    choice = input("local (1) or HS network (2)? ")
    if choice == "1":
        HOST = "localhost"
    elif choice == "2":
        HOST = "10.32.31.18"
    else:
        print("Wrong input detected.")
        exit(1)

    student_id = input("Please enter your student ID: ")
    if len(student_id) != 7:
        print("Student ID has to be 7 digits long.")
        exit(1)

    start_time = time.time()

    bit_length = 3072
    prime = gmpy2.mpz(assets.get_file_content("p.txt"))
    small_a = random.getrandbits(bit_length)
    small_b = random.getrandbits(bit_length)
    base = 2

    fakeA = gmpy2.powmod(base, small_a, prime)
    fakeB = gmpy2.powmod(base, small_b, prime)

    try:
        alice_data = Alice.get_password(student_id, fakeB, "localhost")
    except:
        print("Keine Verbindung zu Alice möglich.")
        exit(1)

    alice_A = gmpy2.mpz(alice_data["decimal"])
    key_alice = assets.calc_hash(alice_A, small_b)
    ct_alice = bytes.fromhex(alice_data["password"])

    pw_decrypted = assets.decrypt_ct(key_alice, ct_alice)

    try:
        valid = Bob.verify_password(student_id, fakeA, small_a, pw_decrypted, "localhost")
    except:
        print("Keine Verbindung zu Bob möglich.")
        exit(1)
 
    if valid:
         print(f"The decrypted password for your student id is: {pw_decrypted}")
         print(f"Process took {time.time()-start_time:.2f}seconds to complete.")
    else: 
        print("Something went wrong!")
        exit()

if __name__ == "__main__":
    main()