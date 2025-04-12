module "aws_users" {
  source           = "./modules/aws"
  users            = var.users
  default_password = var.default_password
}

module "logging" {
  source = "./modules/logging"
}

