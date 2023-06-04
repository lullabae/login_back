/* page 이동할 때마다 로그인 여부 체크 */
export default async function ({ store }) {
    const { isLoggedIn } = store.state.auth
  
    /* vuex state의 로그인 여부 체크 */
    if (isLoggedIn) return
  
    /* vuex state에 로그인 되어 있지 않다고 나오면 API 호출해서 로그인 여부 체크 */
    try {
      await store.dispatch("auth/loginStatusRequest")
    } catch (e) {
      console.log("핸들링 안된 에러 발생")
    }
  }
  