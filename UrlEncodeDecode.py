def encode_url(url: str) -> str:
    return url.replace(" ", "%20")

def decode_url(encoded_url: str) -> str:
    return encoded_url.replace("%20", " ")

URL1 = "http://www.google.com/ this has spaces"
URL2 = "http://www.google.com/this%20has%20no%20spaces"

print("original1: ", URL1)
print("encoded1: ", encode_url(URL1))
print("decoded1: ", decode_url(URL1))

print("original2: ", URL2)
print("encoded2: ", encode_url(URL2))
print("decoded2: ", decode_url(URL2))
