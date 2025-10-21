import streamlit as st

# modules
import config as cf

# title : 타이틀
# header : 헤더 마크다운 
# subheader : 헤더보다 작음
# markdown : 마크 다운 양식 적용 가능, 크기조절도 가능해서 위 기능들보다 일반적으로 사용
# badge : 간단한 배지 표기
# caption: 캡션
# code: 코드
# divider : 구분자 (마크다운으로 해도 됨)
# latext : 수식
# html: html 표기 (마크다운으로 해도 됨)
def show():
    index_num = 1
    cf.desc('title - 제목', index_num)
    st.title('제목')
    index_num += 1
    
    cf.desc('header - 헤더 / 마크다운', index_num)
    st.header('헤더')
    index_num += 1
    
    cf.desc('subheader - 서브 헤더 (헤더보다 작음) / 마크다운', index_num)
    st.subheader('서브헤더')
    index_num += 1
    
    cf.desc('markdown - 마크다운 양식 적용 / 크기 조절도 가능해서 위 속성들보다 일반적으로 사용됨', index_num)
    st.markdown('마크다운')
    st.markdown("""
                마크다운(띄워쓰기 네칸 = 줄바꿈)    
                줄바꿈
                """)
    st.markdown('html을 활용한<br/>줄바꿈', unsafe_allow_html=True)
    index_num += 1
    
    cf.desc('badge - 간단한 뱃지 표기', index_num)
    st.badge('뱃지 - stretch', width='stretch', icon=':material/check:')
    st.badge('뱃지 - content', width='content', icon=':material/check:')
    index_num += 1
    
    cf.desc('caption - 캡션 (주로 설명글)', index_num)
    st.caption('이것은 캡션입니다.')
    index_num += 1
    
    cf.desc('code - 코드블럭', index_num)
    st.code('one_line_code', language="text")
    
    code_python = """
    def hello_python():
        print("HELLO PYTHON!")
    """
    st.code(code_python, language="python")
    
    st.divider()
    
    code_swift = """
    func hello_swift()
        print("HELLO SWIFT")
    """
    st.code(code_swift, language="swift")
    index_num += 1
    
    cf.desc('latex - 수학 표현식', index_num)
    st.latex(r"""result = \frac{a}{b}""")
    index_num += 1
    
    cf.desc('html - html 문법', index_num)
    st.html("""
        <div style="color: red;">빨강</div>
        <div style="color: #00FF00;">초록</div>
        """)