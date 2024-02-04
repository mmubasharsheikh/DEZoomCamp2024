variable "project" {
  description = "ID of project"
  default     = "terraform-demo-412720"
}

variable "region" {
  description = "region of project"
  default     = "us-central1"
}

variable "location" {
  description = "Project location"
  default     = "US"
}

variable "bg_dataset_name" {
  description = "My bigquery dataset name"
  default     = "demo_dataset"
}

variable "gcs_storage_class" {
  description = "Bucket storage class"
  default     = "STANDARD"
}

variable "gcs_bucket_name" {
  description = "Bucket name"
  default     = "terraform-demo-412720-terra-bucket"
}