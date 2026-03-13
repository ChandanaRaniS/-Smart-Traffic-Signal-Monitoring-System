from cryptography import x509  #Imports the x509 module,Used to create SSL/TLS certificates.
from cryptography.x509.oid import NameOID   #certificate identity fields like:Country,Organization,Domain name
from cryptography.hazmat.primitives import hashes, serialization   #hashes → used to digitally sign the certificate,serialization → converts keys to files like .pem
from cryptography.hazmat.primitives.asymmetric import rsa #encryption algorithm.
import datetime

key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "IN"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Karnataka"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "Bangalore"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "CN_Project"),
    x509.NameAttribute(NameOID.COMMON_NAME, "localhost"),
])

cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    key.public_key()
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.datetime.utcnow()
).not_valid_after(
    datetime.datetime.utcnow() + datetime.timedelta(days=365)
).sign(key, hashes.SHA256())

with open("key.pem", "wb") as f:
    f.write(key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ))

with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("SSL certificates generated successfully!")