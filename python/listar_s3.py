import boto3
from botocore.exceptions import ClientError, NoCredentialsError

def listar_buckets_y_objetos():
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        buckets = response.get('Buckets', [])

        if not buckets:
            print("No se encontraron buckets en S3.")
            return

        print("Buckets encontrados en S3:")
        for bucket in buckets:
            bucket_name = bucket['Name']
            print(f"- {bucket_name}")

            try:
                objects = s3.list_objects_v2(Bucket=bucket_name)
                contents = objects.get('Contents', [])

                if not contents:
                    print("  (Sin objetos)")
                else:
                    for obj in contents:
                        print(f"  - {obj['Key']}")
            except ClientError as e:
                print(f"  Error al listar objetos del bucket {bucket_name}: {e}")

    except NoCredentialsError:
        print("No se encontraron credenciales de AWS configuradas.")
    except ClientError as e:
        print(f"Error al conectar con S3: {e}")

if __name__ == "__main__":
    listar_buckets_y_objetos()
