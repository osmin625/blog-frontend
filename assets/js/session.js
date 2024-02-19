// 세션 ID를 가져오는 함수
function getSessionId() {
    // 세션 ID가 이미 존재하는지 확인
    let sessionId = localStorage.getItem('sessionId');

    // 세션 ID가 없으면 새로 생성
    if (!sessionId) {
        sessionId = generateSessionId();
        localStorage.setItem('sessionId', sessionId);
    }

    return sessionId;
}

// 임의의 세션 ID를 생성하는 함수
function generateSessionId() {
    return new Date().getTime().toString(36) + Math.random().toString(36).substr(2, 9); // 임의의 문자열 생성
}