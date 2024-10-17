from curio.storage.files import FileStore
from curio.storage.google_cloud import GoogleCloudFileStore
from curio.storage.local import LocalFileStore
from curio.storage.memory import InMemoryFileStore
from curio.storage.s3 import S3FileStore


def get_file_store(file_store: str, file_store_path: str | None = None) -> FileStore:
    if file_store == 'local':
        if file_store_path is None:
            raise ValueError('file_store_path is required for local file store')
        return LocalFileStore(file_store_path)
    elif file_store == 's3':
        return S3FileStore()
    elif file_store == 'google_cloud':
        return GoogleCloudFileStore()
    return InMemoryFileStore()
