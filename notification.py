import termux_api

def send_termux_notification(title, content):
    """Sends a system notification using Termux API."""
    try:
        # Calls the underlying termux-notification command
        termux.notification(title=title, content=content)
        print(f"Notification sent: '{title}' - '{content}'")
    except Exception as e:
        print(f"Error sending notification: {e}")
        print("Please ensure Termux:API app is installed and permissions are granted.")

# Example usage:
send_termux_notification("Job Done!", "Your Python script has finished running.")
