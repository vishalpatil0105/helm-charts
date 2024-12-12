import yaml
import sys
import pprint

# Get image tag from the command line arguments or use a default value
image_tag = sys.argv[1] if len(sys.argv) > 1 else "test1" 
path = "./helmcharts/python-app/values.yaml"

try:
    # Read the existing YAML file
    with open(path, "r") as file:
        values_file = yaml.safe_load(file)

    # Print the current content for debugging
    print("Before update:")
    pprint.pprint(values_file)

    # Update the image tag
    values_file["image"]["tag"] = image_tag

    # Print the updated content for debugging
    print("After update:")
    pprint.pprint(values_file)

    # Write the updated content back to the YAML file
    with open(path, "w") as file:
        yaml.dump(values_file, file, default_flow_style=False)

    print(f"Updated 'image.tag' to '{image_tag}' in test.yaml successfully!")

except FileNotFoundError:
    print(f"Error: {path} file not found.")
except KeyError as e:
    print(f"Error: Missing key in YAML structure - {e}")
except yaml.YAMLError as exc:
    print(f"Error parsing YAML file: {exc}")
