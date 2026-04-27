# 스터디 12주차 발표 (교육 파트)

### 주제 : LTI 1.3 Advantage를 통한 교육 시스템 통합 및 데이터 환류 아키텍처

## 0. 서론: '데이터 저장'에서 '시스템 가상 통합'으로

지난 11주차 발표에서는 xAPI를 통해 파편화된 학습 경험 데이터를 표준화하여 LRS에 저장하는 인프라를 다루었다. 하지만 데이터가 저장되는 것과 별개로, 학습자가 여러 교육 도구를 이동할 때마다 발생하는 **인증(Auth)의 번거로움**과 **도구 간 보안 통신**의 문제는 해결되지 않은 상태였다.

12주차 발표에서는 외부 교육 도구를 중앙 LMS에 로그인 없이 안전하게 연결하고, 학습 결과를 자동으로 회수하는 **LTI 1.3 Advantage** 표준을 다룬다.

※ **LTI (Learning Tools Interoperability):** LMS와 외부 도구(Tool) 간의 안전한 연동을 지원하는 표준 인터페이스 규격.

## 1. 문제 제기: 파편화된 도구와 수동 데이터 관리의 한계

- **인증의 분절(Authentication Silo):** 학습자가 LMS에서 외부 코딩 실습 환경으로 이동할 때마다 별도의 계정 로그인이 필요하며, 이는 학습 몰입(Flow)을 저해한다.
- **보안 취약점:** 단순 링크 공유 방식은 URL 탈취를 통한 대리 출석이나 성적 조작의 위험이 존재한다.
- **성적 데이터의 수동 기입:** 외부 도구에서 수행한 과제 결과가 LMS 성적부(Gradebook)와 동기화되지 않아 교육자가 데이터를 수동으로 옮겨야 하는 행정적 비효율이 발생한다.

👉 수많은 외부 교육 도구들을 어떻게 로그인 장벽 없이(SSO) 안전하게 통합하고, 학습 결과 데이터를 중앙 LMS로 자동 동기화하는 '표준화된 신경망'을 구축할 수 있을까?

※ SSO (Single Sign-On, 통합인증) : 한 번의 로그인으로 구글, AWS, 사내 시스템 등 여러 애플리케이션 및 서비스에 자동으로 인증되어 추가 로그인 없이 접근할 수 있는 기술

---

## 2. 핵심 기술 : LTI 1.3 Advantage

최신 표준인 **LTI 1.3 Advantage**는 단순한 연결을 넘어, 교육 도구 통합에 필요한 세 가지 필수 서비스를 패키지로 제공한다.

| 서비스 명칭 | 주요 기능 | 교육적 가치 |
| --- | --- | --- |
| **Deep Linking** | LMS 내에서 외부 도구의 특정 콘텐츠(예: 특정 문제)를 선택하여 직접 배치 | 교수자가 필요한 학습 자원을 자유롭게 조립(Orchestration) 가능 |
| **AGS (Assignment & Grades)** | 외부 도구에서 산출된 점수와 피드백을 LMS 성적부로 즉시 전송 | 수동 성적 입력의 행정적 비효율 제거 및 데이터 실시간성 확보 |
| **NRPS (Names & Role)** | LMS의 수강생 명단과 역할을 외부 도구로 실시간 동기화 | 도구 내 별도 사용자 등록 과정 없이 즉각적인 학습 환경 조성 |

**※ Why LTI 1.3?** 이전 버전(1.1)과 달리 최신 표준은 **비대칭 키 암호화**를 사용하여 데이터 전송 구간에서 해킹이나 위변조가 불가능하도록 설계되었다.

### LTI 1.3 Advantage의 기술적 메커니즘

LTI 1.3은 **OIDC(OpenID Connect)**와 **OAuth 2.0**을 기반으로 한 신뢰 기반의 메시징 체계를 갖추고 있다. 실제 인증 및 데이터 교환은 다음의 4단계 과정을 거친다.

1. **OIDC 로그인 요청**
    
    LMS → Tool
    
    사용자가 LMS 내 과제를 클릭하면, LMS는 도구의 '로그인 시작 URL'로 OIDC 요청을 보낸다.
    
2. **인증 및 응답**
    
    Tool → LMS
    
    도구는 LMS의 인증 엔드포인트로 사용자를 리다이렉트하여 정당한 사용자인지 확인을 요청한다.
    
3. **ID Token 전달**
    
    LMS → Tool (JWT)
    
    인증이 완료되면 LMS는 사용자 정보와 과제 정보를 담은 *JWT(JSON Web Token)*를 서명하여 도구에 POST로 전송한다.
    
4. **Access Token 및 서비스 호출**
    
    Tool → LMS (OAuth 2.0)
    
    도구는 전달받은 JWT를 검증한 후, OAuth 2.0을 통해 **Access Token**을 발급받아 LMS의 성적부 서비스(*AGS*) API를 호출해 점수를 전송한다.
    

※ **JWT (JSON Web Token):** 인증에 필요한 정보를 암호화하여 담은 JSON 기반의 토큰.
※ **AGS (Assignment and Grades Services):** 외부 도구가 LMS 성적부에 직접 점수를 기록할 수 있게 해주는 핵심 서비스.

---

## 3. 활용 방안: xAPI와 LTI의 데이터 결합 구조 (Analytics Layer)

단순히 점수만 받는 것이 아니라, 11주차에 다룬 xAPI와 결합하여 **'성장 궤적'**을 입체적으로 분석한다.

- **xAPI (행동 로그):** 학습자가 실습 도구 내에서 보낸 시간, 클릭 횟수, 코드 수정 횟수 등을 실시간으로 **LRS**에 전송한다.
- **LTI (결과 데이터):** 실습이 종료된 후, 최종 도출된 성적(Score)이나 합격 여부(Pass/Fail)를 **LMS Gradebook**으로 전송한다.
- **통합 대시보드:** 관리자는 `User ID`를 기준으로 두 데이터를 결합하여 "A 학습자는 특정 구간에서 20번의 코드 수정(xAPI) 끝에 90점(LTI)을 획득했다"는 인과관계를 분석할 수 있다.

Example)

- **xAPI (과정 데이터):** "학습자가 코드를 수정하는 데 15분을 소요했으며, 특정 API 레퍼런스를 5번 참조함" → **LRS 저장 (행동 분석)**
- **LTI (결과 데이터):** "최종 과제 제출 결과 95점을 획득하였으며, 합격 처리됨" → **LMS Gradebook 전송 (성적 관리)**
- **시너지:** 두 데이터를 결합하여 학습 효율성이 낮은 구간(xAPI)과 최종 성취도(LTI) 사이의 상관관계를 분석함으로써, 10주차에 논의한 지능형 피드백(LLM)의 정교함을 극대화할 수 있다.

---

## 4. 활용 사례

### 사례 1: GitHub Classroom & LMS 연동

LMS 내에서 GitHub 과제를 생성하고, 학생의 GitHub 계정을 LMS 계정과 매핑한다. 자동 채점 결과가 LMS 성적표에 즉각 반영되는 가장 대표적인 사례이다.

**※** 참고 자료 **:** [GitHub Docs - Connect a learning management system course to a classroom](https://docs.github.com/en/education/manage-coursework-with-github-classroom/teach-with-github-classroom/connect-a-learning-management-system-course-to-a-classroom)

### 사례 2: *Gradescope* (LTI 1.3의 표준 모델)

LTI 1.3의 NRPS(명단 동기화) 서비스를 사용하여 LMS 수강생 목록을 가져오고, 채점이 끝나면 AGS(성적 전송 서비스)를 통해 LMS로 결과를 환류한다.

**※** 참고 자료 **:** [Gradescope Help - Configuring Gradescope LTI 1.3 in Canvas](https://guides.gradescope.com/hc/en-us/articles/21759105768845-Configuring-Gradescope-LTI-1-3-in-Canvas-for-Admins)

※ **Gradescope** : 채점, 학습 관리, 첨삭 피드백 등의 기능을 제공하는 비대면 평가 지원 도구

---

## 5. 의의 및 한계 (극복 방안 포함)

- **의의:** 표준 규격만 준수하면 어떤 새로운 에듀테크 도구도 기존 인프라에 즉각 통합할 수 있는 **’플러그 앤 플레이(Plug-and-Play)'**를 실현한다.
- **한계:** LTI 1.3은 JWT 서명 및 공개키 교환(JWKS) 등 보안 구현 난이도가 높다.
- **극복 방안 :** 검증된 오픈소스 라이브러리(`pylti1.3`, `lti-1-3-php-library` 등)를 적극 도입하고, IMS Global에서 제공하는 **LTI Reference Implementation** 도구를 활용하여 실시간으로 정합성을 테스트한다.

## 6. 결론

11주차의 **xAPI가 학습의 '과정'**을 풍부하게 기록한다면, 12주차의 **LTI는 시스템 간 '신경망'** 역할을 한다. 이 두 표준이 결합될 때 비로소 보안과 데이터가 하나로 통합된 완성형 에듀테크 시스템이 완성된다.