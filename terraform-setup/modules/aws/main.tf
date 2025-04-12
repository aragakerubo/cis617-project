resource "aws_iam_user" "multi_users" {
  for_each = toset(var.users)
  name     = each.value

  tags = {
    Simulation = "BruteForceTest"
  }
}

resource "aws_iam_user_login_profile" "login" {
  for_each                 = aws_iam_user.multi_users
  user                     = each.value.name
  password_reset_required  = false
}

resource "aws_iam_user_policy_attachment" "readonly_attach" {
  for_each   = aws_iam_user.multi_users
  user       = each.value.name
  policy_arn = "arn:aws:iam::aws:policy/ReadOnlyAccess"
}

output "created_users" {
  value = keys(aws_iam_user.multi_users)
}

