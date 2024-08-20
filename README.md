# balcts-api-server

이 프로젝트는 Django 기반의 API 서버로, CRUD 작업을 제공합니다.

## 목차

- [프로젝트 개요](#프로젝트-개요)
- [기능](#기능)
- [설치 방법](#설치-방법)
- [사용법](#사용법)
- [API 엔드포인트](#api-엔드포인트)


## 프로젝트 개요

`balcts-api-server`는 Django 애플리케이션입니다. 데이터의 생성, 조회, 업데이트, 삭제를 위한 엔드포인트를 포함하고 있습니다.

## 기능

- **CRUD 작업**: 데이터의 생성, 조회, 업데이트, 삭제 작업 지원.
- **RESTful API**: 백엔드와의 상호작용을 위한 RESTful API 제공.
- **Django Admin**: 애플리케이션 데이터를 쉽게 관리할 수 있는 Django Admin 통합.
- **인증**: Django의 내장 기능을 사용한 기본 인증 설정.

## 설치 방법

해당 프로젝트의 DB는 postgresql로 설정으로 되어 있어 로컬에 DB가 먼저 구동되어 있어야지만 유효합니다. 프로젝트 구축은 쿠버네티스 레포지토리를 참고해주세요:

아래는 장고 내 SQLite를 활용했을 때 프로젝트 구축 순서입니다.

1. **레포지토리 클론**

    ```bash
    git clone git@github.com:42jasuh/balcts-api-server.git
    cd balcts-api-server
    ```

2. **가상 환경 설정**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows에서는 `venv\Scripts\activate` 사용
    ```

3. **종속성 설치**

    ```bash
    pip install -r requirements.txt
    ```

4. **마이그레이션 적용**

    ```bash
    DB가 postgresql로 설정이 되어 있어 로컬에 DB가 먼저 구동되어 있어야지만 유효합니다.
    python manage.py migrate
    ```

5. **개발 서버 실행**

    ```bash
    DB가 postgresql로 설정이 되어 있어 로컬에 DB가 먼저 구동되어 있어야지만 유효합니다.
    python manage.py runserver
    ```

## 사용법

서버가 실행되고 나면, API 엔드포인트에 `http://127.0.0.1:8000/`에서 접근할 수 있습니다.

Django Admin 인터페이스에 접근하려면 `http://127.0.0.1:8000/admin/`로 이동하여 슈퍼유저 자격증명으로 로그인 가능

## API 엔드포인트

### 예제 엔드포인트

- **게시물 생성**
    - `POST /post/`
    - 요청 본문: `{ "title": "예제 제목", "content": "예제 내용" }`

- **게시물 조회**
    - `GET /post/`

- **특정 게시물 조회**
    - `GET /post/{id}/`

- **게시물 업데이트**
    - `PUT /post/{id}/`
    - 요청 본문: `{ "title": "업데이트된 제목", "content": "업데이트된 내용" }`

- **게시물 삭제**
    - `DELETE /post/{id}/`
