import os
from datetime import datetime

GIT_USERNAME = "sdg877"
GIT_EMAIL = "sdrakegill@gmail.com"
LOG_FILE = "log.md"

# --- Script Logic ---
def create_log_entry():
    """Generates a simple, timestamped log entry."""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    entry = f"### Daily Log Entry for {date_str}\n\n* Ran script at {time_str}\n\n---\n\n"
    return entry

def add_and_commit():
    """Adds, commits, and pushes the changes to GitHub."""
    # Configure Git user details for the commit
    os.system(f'git config user.name "{GIT_USERNAME}"')
    os.system(f'git config user.email "{GIT_EMAIL}"')
    
    # Add the log file to the staging area
    os.system(f'git add {LOG_FILE}')
    
    # Commit the changes with a timestamped message
    commit_message = f"Daily automated log on {datetime.now().strftime('%Y-%m-%d')}"
    os.system(f'git commit -m "{commit_message}"')
    
    # Push the changes to the remote repository
    os.system('git push origin main')

def main():
    """Main function to run the logging process."""
    print("Generating a new log entry...")
    log_entry = create_log_entry()

    # Append the new entry to the log file
    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)
    
    print("Log entry created. Committing and pushing to GitHub...")
    try:
        add_and_commit()
        print("Success! Changes pushed to GitHub.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Make sure you have configured your Git credentials.")

if __name__ == "__main__":
    main()