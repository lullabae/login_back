SELECT_USER_INFO = """
SELECT *
  FROM USERS.USER_INFO
 WHERE USER_ID = %(user_id)s 
   AND USER_NM  %(user_nm)s
"""

SELECT_USER = """
SELECT `USER_ID`
     , `USER_PW`
     , `USER_NM`
  FROM USERS.USER_INFO
 WHERE USER_ID = %(user_id)s
"""
SELECT_USER_LOGIN_ID_PW = """
SELECT * 
  FROM USERS.USER_INFO
 WHERE USER_ID = %(user_id)s
   AND USER_PW = %(user_pw)s
;
"""
INSERT_USER = """
INSERT INTO USERS.USER_INFO(
  `USER_ID`,`USER_PW`, `USER_NM`)
VALUE(
  %(user_id)s, %(user_pw)s, %(user_nm)s
);
"""