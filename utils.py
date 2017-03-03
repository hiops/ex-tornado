import hashlib

def gen_hash(str,salt):
    return hashlib.sha1(str + salt).hexdigest()
def check_hash(str_hash,str_raw,salt):
    if str_hash == gen_hash(str_raw,salt):
        return True
    else:
        return False

if __name__ == "__main__":
    print gen_hash('123456','secret')
    print check_hash('c5aa204c1a554e42ed682459e91f7c86b1d34acb','123456', 'secret')
