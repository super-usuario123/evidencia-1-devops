import boto3
from botocore.exceptions import ClientError, NoCredentialsError
import argparse

REGION = "us-west-2"

def listar_instancias():
    try:
        ec2 = boto3.client("ec2", region_name=REGION)
        response = ec2.describe_instances()

        found = False
        for reservation in response.get("Reservations", []):
            for instance in reservation.get("Instances", []):
                found = True
                instance_id = instance.get("InstanceId", "N/A")
                state = instance.get("State", {}).get("Name", "N/A")
                instance_type = instance.get("InstanceType", "N/A")
                public_ip = instance.get("PublicIpAddress", "Sin IP pública")

                print(f"ID: {instance_id}")
                print(f"Estado: {state}")
                print(f"Tipo: {instance_type}")
                print(f"IP pública: {public_ip}")
                print("-" * 40)

        if not found:
            print(f"No se encontraron instancias EC2 en la región {REGION}.")

    except NoCredentialsError:
        print("No se encontraron credenciales de AWS configuradas.")
    except ClientError as e:
        print(f"Error al listar instancias: {e}")

def iniciar_instancia(instance_id):
    try:
        ec2 = boto3.client("ec2", region_name=REGION)
        ec2.start_instances(InstanceIds=[instance_id])
        print(f"La instancia {instance_id} se está iniciando.")
    except NoCredentialsError:
        print("No se encontraron credenciales de AWS configuradas.")
    except ClientError as e:
        print(f"Error al iniciar la instancia: {e}")

def detener_instancia(instance_id):
    try:
        ec2 = boto3.client("ec2", region_name=REGION)
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"La instancia {instance_id} se está deteniendo.")
    except NoCredentialsError:
        print("No se encontraron credenciales de AWS configuradas.")
    except ClientError as e:
        print(f"Error al detener la instancia: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Gestión básica de instancias EC2")
    parser.add_argument("--action", choices=["list", "start", "stop"], required=True, help="Acción a realizar")
    parser.add_argument("--instance-id", help="ID de la instancia EC2")

    args = parser.parse_args()

    if args.action == "list":
        listar_instancias()
    elif args.action == "start":
        if not args.instance_id:
            print("Debes proporcionar --instance-id para iniciar una instancia.")
        else:
            iniciar_instancia(args.instance_id)
    elif args.action == "stop":
        if not args.instance_id:
            print("Debes proporcionar --instance-id para detener una instancia.")
        else:
            detener_instancia(args.instance_id)
