provider "aws" {
  region = "us-west-2"
}

resource "aws_rds_instance" "nasa_rds" {
  allocated_storage    = 20
  engine               = "postgres"
  instance_class       = "db.t2.micro"
  name                 = "nasa_data_db"
  username             = var.db_username
  password             = var.db_password
  skip_final_snapshot  = true
}

resource "aws_s3_bucket" "nasa_data_bucket" {
  bucket = "nasa-etl-bucket"
  acl    = "private"
}