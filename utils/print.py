def print_job_info(fine_tuning_job):
    print(f"Fine-tuning job ID: {fine_tuning_job.id}")
    print(f"Fine-tuning job model: {fine_tuning_job.model}")
    print(f"Fine-tuning job error: {fine_tuning_job.error}")
    print(f"Fine-tuning job created at: {fine_tuning_job.created_at}")
    print(f"Fine-tuning job training file: {fine_tuning_job.training_file}")
    
    