# Roblox Group Wall Purger

**Roblox Group Wall Purger** is a Python script designed to help manage and clean up posts on your Roblox group wall. This script can delete posts containing specific keywords, making it easier to maintain a clean and relevant group wall.

## Use Cases

1. **Maintaining Group Cleanliness**: If you manage a group and want to ensure that the wall is free from spam or irrelevant content, this script helps you filter and remove such posts.
2. **Hiding Past Content**: You can use the script to find and delete old posts that no longer reflect the current status or direction of the group.
3. **Improving Group Reputation**: By cleaning up posts that may negatively impact the group’s image, you can present a more polished and professional appearance.
4. **Managing Sensitive Information**: If your group wall has posts that contain sensitive or outdated information, this script helps you locate and remove them.

## Features

- **Collects Posts**: Retrieves all posts from the specified group wall, handling pagination to ensure all posts are processed.
- **Filters Posts**: Identifies posts containing user-defined keywords.
- **Prompts for Action**: Displays posts with the specified keywords and asks for user confirmation before deleting.
- **Deletes Posts**: Removes posts based on user input.

## Requirements

- Python 3.x
- `requests` library
- `tqdm` library (for progress bar)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Ghosty-Tongue/roblox-group-wall-purger.git
    ```
2. **Navigate to the directory**:
    ```bash
    cd roblox-group-wall-purger
    ```
3. **Install the required libraries**:
    ```bash
    pip install requests tqdm
    ```

## Usage

1. **Run the script**:
    ```bash
    python delete.py
    ```
2. **Enter the required inputs**:
    - **Group ID**: The ID of the Roblox group whose wall posts you want to manage.
    - **.ROBLOSECURITY Cookie**: Your Roblox session cookie. This is required for authentication.
    - **Keywords**: Enter keywords to search for in the posts. You can specify multiple keywords separated by commas.

3. **Follow the prompts**:
    - The script will collect all posts from the group wall and display those that contain the specified keywords.
    - It will ask for confirmation before deleting the posts. Confirm with 'Y' to delete or 'N' to skip deletion.

## Example

```text
Enter the group ID: 12345678
Enter your .ROBLOSECURITY cookie: your_roblosecurity_cookie
Enter keywords to search for (separate multiple keywords with commas): runner, runners

Collecting posts: 1901it [00:15, 127.42it/s]

Posts containing the specified keywords:
1. Post ID: 6294954412, Content: This is a post with the word runner.
2. Post ID: 6294952804, Content: Another post mentioning runners.

Do you want to delete all the above 2 posts? (Y/N): Y
Successfully deleted post 6294954412
Successfully deleted post 6294952804
```

## Notes

- The script handles pagination to ensure all posts are collected and processed.
- If too many requests are made, the script will wait for 30 seconds before retrying.
- The CSRF token is refreshed automatically if it becomes invalid.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

Use this script responsibly. Deleting posts cannot be undone. Ensure you have proper permissions to manage the group wall and handle your cookies securely.

---

For any issues or feature requests, please open an issue on the [GitHub repository](https://github.com/Ghosty-Tongue/roblox-group-wall-purger/issues).
