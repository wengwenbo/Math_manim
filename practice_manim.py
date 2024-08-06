from manim import *

class SubtractEquations(Scene):
    def construct(self):
        # 创建公式对象
        equation1 = MathTex("a + b = c")
        equation2 = MathTex("a - b = d")
        equation3 = MathTex("c - d = b")
        
        # 设置初始位置
        equation1.shift(UP)
        equation2.shift(DOWN)
        equation3.shift(DOWN * 2)
        
        # 添加到场景
        self.add(equation1, equation2)
        
        # 动画效果：将equation1和equation2相减得到equation3
        self.play(TransformFromCopy(equation1, equation3))
        self.wait()

