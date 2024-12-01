import logging


def logger_config(module):
    """
    配置日志记录器函数。扩展了Python的logging模块并设置自定义配置。
    参数: 模块名称。例如: logger_config(__name__)。
    返回: 自定义的日志记录器对象。
    """
    # 创建日志消息格式
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

    # 创建一个处理器，将日志输出到标准错误流
    handler = logging.StreamHandler()
    # 为处理器设置日志消息格式
    handler.setFormatter(formatter)

    # 使用指定的模块名称创建一个日志记录器对象
    custom_logger = logging.getLogger(module)
    # 将日志记录器对象的日志级别设置为DEBUG
    custom_logger.setLevel(logging.DEBUG)

    # 将处理器添加到日志记录器对象
    custom_logger.addHandler(handler)

    # 返回自定义的日志记录器对象
    return custom_logger
