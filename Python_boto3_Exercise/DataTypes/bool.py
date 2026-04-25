enable_autoscaling = True
is_production = False
if enable_autoscaling:
    print("Autoscaling is enabled.")
if is_production:
    print("This is a production environment.")
else:
    print("This is a non-production environment.")  