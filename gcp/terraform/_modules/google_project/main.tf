resource "google_project" "my-project-in-a-folder" {
  name 	      = "my-project"
  project_id = "your-project-id"
  folder_id  = "${google_folder.department-1.name}"
}