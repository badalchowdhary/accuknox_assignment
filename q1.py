# Q1

# By default, Django signals are executed synchronously.



@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(5) 
    print("Signal handler finished")

def create_user():
    print("Creating user...")
    user = User.objects.create(username='testuser')
    print("User created")

create_user()


# Output

# Creating user...
# Signal handler started
# # (5 seconds delay)
# Signal handler finished
# User created
