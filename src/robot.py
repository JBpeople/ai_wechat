import re
import requests

_API_BASE = "https://api.aabao.vip/"
_API_KEY = "sk-vf4HdR5cIJqPV9350bEf68E0F9E3492dB79d68B6B9006096"


def _handle_response(response: str) -> str:
    """处理AI回答

    Args:
        response (str): AI回答

    Returns:
        str: 处理后的AI回答
    """
    ad_pat = re.compile(r"\[.*?\]")
    response = ad_pat.sub("", response)
    response = response.strip()
    return response


def get_response(prompt: str) -> str:
    """获取AI回答

    Args:
        prompt (str): 用户输入

    Raises:
        e: 请求失败

    Returns:
        str: AI回答
    """
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {_API_KEY}",
        "User-Agent": "Apifox/1.0.0 (https://apifox.com)",
        "Content-Type": "application/json",
    }

    resp = requests.post(
        f"{_API_BASE}v1/chat/completions",
        json={
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": prompt}],
        },
        headers=headers,
    )
    try:
        content = resp.json()["choices"][0]["message"]["content"]
        content = _handle_response(content)
    except Exception as e:
        print(resp.json())
        raise e

    return content
