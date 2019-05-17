import json
import sys


def main():
    workspace_name = sys.argv[1]

    markdown_file = open("nlu.md", "w+")

    with open(workspace_name, 'r') as workspace_json:
        workspace = json.load(workspace_json)
        intents = workspace["intents"]

        for intent in intents:
            intent_name = intent["intent"]
            intent_examples = intent["examples"]
            print("\n## intent:", intent_name)
            intent_md_str = "\n## intent: " + intent_name + "\n"
            markdown_file.write(intent_md_str)
            for intent_example in intent_examples:
                intent_example_text = intent_example["text"]
                print(" -", intent_example_text)
                example_md_str = " - " + intent_example_text + "\n"
                markdown_file.write(example_md_str)

        markdown_file.close()


if __name__ == "__main__":
    main()
