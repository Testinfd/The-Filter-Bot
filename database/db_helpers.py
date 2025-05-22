# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pymongo import MongoClient
import motor.motor_asyncio
import ssl

def get_mongo_client(uri):
    """
    Create a MongoDB client with proper TLS/SSL settings.
    This resolves the SSL handshake failures with MongoDB Atlas.
    """
    if not uri:
        return None
    
    # Configure TLS/SSL options
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    
    # Connect with TLS/SSL options
    return MongoClient(
        uri,
        ssl=True,
        ssl_cert_reqs=ssl.CERT_NONE,
        tlsAllowInvalidCertificates=True
    )

def get_async_mongo_client(uri):
    """
    Create an asynchronous MongoDB client with proper TLS/SSL settings.
    For Motor AsyncIOMotorClient connections.
    """
    if not uri:
        return None
    
    # Connect with TLS/SSL options
    return motor.motor_asyncio.AsyncIOMotorClient(
        uri,
        ssl=True,
        ssl_cert_reqs=ssl.CERT_NONE,
        tlsAllowInvalidCertificates=True
    ) 