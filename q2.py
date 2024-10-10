# Q2

# Yes, by default, Django signals run in the same thread as the caller.

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")

def create_user():
    print(f"Main thread: {threading.current_thread().name}")
    user = User.objects.create(username='testuser')

create_user()

# Output

# Main thread: MainThread
# Signal handler thread: MainThread