import hashlib

#define a string to hash    
string_to_hash = "Hello, World!"

#create a hash object using the SHA256 algorithm
hash_object = hashlib.sha256()

#update the hash object with the string to hash
hash_object.update(string_to_hash.encode())

#get the hash value as a hex string
hash_value = hash_object.hexdigest()

print("Original string: ", string_to_hash)
print("Hash value: ", hash_value)




# SHA-256 is a cryptographic hash function that takes an input of arbitrary length and produces a fixed-size output of 256 bits. It is part of the SHA-2 family of hashing algorithms, which includes several other hash functions with different output sizes (e.g. SHA-224, SHA-384, SHA-512).

# SHA-256 is widely used in computer security and cryptography, for applications such as digital signatures, password storage, and message authentication codes. It is considered to be a secure hashing algorithm, as it is very difficult (infeasible) to reverse-engineer the input data from the hash value.

# The basic idea behind the SHA-256 algorithm is to take the input data and process it through a series of mathematical operations that produce a fixed-size output. This processing involves several steps, including padding the input data to a multiple of 512 bits, breaking the padded data into 512-bit chunks, and applying a series of rounds that involve bitwise operations, modular addition, and other operations.

# One important property of the SHA-256 algorithm is that even small changes to the input data will produce a completely different hash value. This is known as the avalanche effect and is a desirable property of secure hash functions.

# Overall, SHA-256 is a widely used and well-regarded hashing algorithm that provides a high level of security for many applications.