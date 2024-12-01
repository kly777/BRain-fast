import secrets

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from api.config import settings

# 初始化HTTP基础认证，设置为不自动引发错误，以便自定义错误处理
basic_auth = HTTPBasic(auto_error=False)


def authent(
    credentials: HTTPBasicCredentials = Depends(basic_auth),
):
    """
    认证函数，用于验证用户提供的用户名和密码是否正确。

    Args:
        credentials (HTTPBasicCredentials): 用户提供的认证信息，包括用户名和密码。

    Raises:
        HTTPException: 如果认证失败，则抛出403状态码的HTTP异常。

    Returns:
        bool: 如果认证成功，返回True。
    """
    if check_basic_auth_creds(credentials):
        return True

    raise HTTPException(status_code=403, detail="invalid user/password provided")


def check_basic_auth_creds(
    credentials: HTTPBasicCredentials = Depends(basic_auth),
):
    """
    检查基础认证的凭据是否正确。

    Args:
        credentials (HTTPBasicCredentials): 用户提供的认证信息，包括用户名和密码。

    Returns:
        bool: 如果用户名和密码都正确，返回True，否则返回False。
    """
    # 使用安全的方式比较用户名和密码，防止时序攻击
    correct_username = secrets.compare_digest(
        credentials.username, settings.API_USERNAME
    )
    correct_password = secrets.compare_digest(
        credentials.password, settings.API_PASSWORD
    )

    if correct_username and correct_password:
        return True

    return False
