import boto3
from botocore.exceptions import ClientError, NoCredentialsError

REGION = "us-west-2"
OUTPUT_FILE = "python/reporte_recursos.txt"

def generar_reporte():
    try:
        ec2 = boto3.client("ec2", region_name=REGION)
        response = ec2.describe_instances()

        lineas = []
        lineas.append("REPORTE DE RECURSOS AWS")
        lineas.append(f"Región: {REGION}")
        lineas.append("=" * 50)

        found = False
        for reservation in response.get("Reservations", []):
            for instance in reservation.get("Instances", []):
                found = True
                instance_id = instance.get("InstanceId", "N/A")
                state = instance.get("State", {}).get("Name", "N/A")
                instance_type = instance.get("InstanceType", "N/A")
                public_ip = instance.get("PublicIpAddress", "Sin IP pública")

                lineas.append(f"ID: {instance_id}")
                lineas.append(f"Estado: {state}")
                lineas.append(f"Tipo: {instance_type}")
                lineas.append(f"IP pública: {public_ip}")
                lineas.append("-" * 50)

        if not found:
            lineas.append("No se encontraron instancias EC2 en esta región.")

        with open(OUTPUT_FILE, "w", encoding="utf-8") as archivo:
            for linea in lineas:
                archivo.write(linea + "\n")

        print(f"Reporte generado correctamente en: {OUTPUT_FILE}")

    except NoCredentialsError:
        print("No se encontraron credenciales de AWS configuradas.")
    except ClientError as e:
        print(f"Error al generar el reporte: {e}")

if __name__ == "__main__":
    generar_reporte()
