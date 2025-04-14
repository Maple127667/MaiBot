# from src.plugins.person_info.relationship_manager import relationship_manager
from src.common.logger import get_module_logger
from src.do_tool.tool_can_use.base_tool import BaseTool
# from src.plugins.chat_module.think_flow_chat.think_flow_generator import ResponseGenerator


logger = get_module_logger("relationship_tool")

class RelationshipTool(BaseTool):
    name = "change_relationship"
    description = "根据收到的文本和回复内容，修改与特定用户的关系值，当你回复了别人的消息，你可以使用这个工具"
    parameters = {
        "type": "object",
        "properties": {
            "text": {
                "type": "string",
                "description": "收到的文本"
            },
            "changed_value": {
                "type": "number",
                "description": "变更值"
            },
            "reason": {
                "type": "string",
                "description": "变更原因"
            }
        },
        "required": ["text", "changed_value", "reason"]
    }
        

    async def execute(self, args: dict,message_txt:str) -> dict:
        """执行工具功能
        
        Args:
            args: 包含工具参数的字典
            text: 原始消息文本
            changed_value: 变更值
            reason: 变更原因
            
        Returns:
            dict: 包含执行结果的字典
        """
        try:
            text = args.get("text")
            changed_value = args.get("changed_value")
            reason = args.get("reason")
        
            return {"content": f"因为你刚刚因为{reason}，所以你和发[{text}]这条消息的人的关系值变化为{changed_value}"}

        except Exception as e:
            logger.error(f"修改关系值时发生错误: {str(e)}")
            return {"content": f"修改关系值失败: {str(e)}"} 