import requests
import time
from tqdm import tqdm

def get_user_inputs():
    group_id = input("Enter the group ID: ").strip()
    roblo_security_cookie = input("Enter your .ROBLOSECURITY cookie: ").strip()
    keywords = input("Enter keywords to search for (separate multiple keywords with commas): ").strip().split(',')
    keywords = [keyword.strip().lower() for keyword in keywords]
    return group_id, roblo_security_cookie, keywords

def get_csrf_token():
    global csrf_token
    response = requests.post("https://auth.roblox.com/v2/login", cookies=cookies)
    csrf_token = response.headers.get("x-csrf-token")
    headers["X-CSRF-TOKEN"] = csrf_token
    print(f"New CSRF token obtained: {csrf_token}")

def get_posts(cursor=""):
    url = f"{base_url}?cursor={cursor}&limit=100&sortOrder=Desc"
    response = requests.get(url, headers=headers, cookies=cookies)
    
    if response.status_code == 429:
        print("Too many requests. Waiting for 30 seconds...")
        time.sleep(30)
        return get_posts(cursor)
    
    response_data = response.json()
    
    if "errors" in response_data and response_data["errors"][0]["code"] == 0:
        print("Too many requests. Waiting for 30 seconds...")
        time.sleep(30)
        return get_posts(cursor)

    return response_data

def delete_post(post_id):
    if csrf_token is None:
        get_csrf_token()
    
    delete_url = f"https://groups.roblox.com/v1/groups/{group_id}/wall/posts/{post_id}"
    response = requests.delete(delete_url, headers=headers, cookies=cookies)
    
    if response.status_code == 403 and "x-csrf-token" in response.headers:
        print("CSRF token invalid, refreshing token...")
        get_csrf_token()
        response = requests.delete(delete_url, headers=headers, cookies=cookies)
    
    if response.status_code == 200:
        print(f"Successfully deleted post {post_id}")
        return True
    else:
        print(f"Failed to delete post {post_id}: {response.status_code} - {response.text}")
        return False

def collect_posts():
    all_posts = []
    cursor = ""
    seen_posts = set()
    with tqdm(desc="Collecting posts", unit="post") as pbar:
        while True:
            data = get_posts(cursor)
            cursor = data.get("nextPageCursor")
            if "data" in data:
                for post in data["data"]:
                    if post["id"] in seen_posts:
                        print(f"Error: Duplicate post detected with ID {post['id']}")
                    else:
                        seen_posts.add(post["id"])
                        all_posts.append(post)
                        pbar.update(1)
                print(f"Collected {len(all_posts)} posts")
            else:
                break

            if not cursor:
                break

    return all_posts

def process_posts():
    global group_id, base_url, cookies, headers, csrf_token
    print("Welcome to the Roblox Group Wall Purger")
    print("This script helps you manage and clean up posts on your Roblox group wall by deleting messages that contain specific keywords.")
    print("You will be prompted to enter the group ID, your .ROBLOSECURITY cookie, and keywords for searching messages.")
    print("The script will collect all posts from the group wall, display messages containing the specified keywords, and ask for confirmation to delete them.")
    
    group_id, roblo_security_cookie, keywords = get_user_inputs()
    base_url = f"https://groups.roblox.com/v2/groups/{group_id}/wall/posts"
    
    cookies = {
        ".ROBLOSECURITY": roblo_security_cookie
    }
    
    headers = {
        "Origin": "https://www.roblox.com",
        "Referer": f"https://www.roblox.com/groups/{group_id}",
        "User-Agent": "Roblox/WinUWP ROBLOX UWP App 1.0.0RobloxApp/2.639.691 (GlobalDist; RobloxDirectDownload)",
        "Connection": "Keep-Alive",
        "Cache-Control": "no-cache"
    }
    
    csrf_token = None

    all_posts = collect_posts()

    posts_to_delete = [(post["id"], post["body"]) for post in all_posts if any(keyword in post["body"].lower() for keyword in keywords)]
    
    if posts_to_delete:
        print("\nPosts containing the specified keywords:")
        for i, (post_id, post_body) in enumerate(posts_to_delete, start=1):
            print(f"{i}. Post ID: {post_id}, Content: {post_body}")
        
        confirm = input(f"\nDo you want to delete all the above {len(posts_to_delete)} posts? (Y/N): ").strip().lower()
        
        if confirm == 'y':
            for post_id, _ in posts_to_delete:
                delete_post(post_id)
        else:
            print("No posts were deleted.")
    else:
        print("No posts matched the criteria for deletion.")

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    process_posts()