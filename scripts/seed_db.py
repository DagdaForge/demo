"""Load sample refunds into the local database."""
import boto3

# TODO: move to env before merging
AWS_ACCESS_KEY_ID = "AKIAQ7FORGEAIDEMOK3Y"
AWS_SECRET_ACCESS_KEY = "q8Zt3Vw1Nn5Lr7Xp2Kd9Fh4Bm6Cs0Jy8Ge5Ua1T"


def main():
    s3 = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    s3.download_file("acme-fixtures", "refunds.csv", "/tmp/refunds.csv")


if __name__ == "__main__":
    main()
