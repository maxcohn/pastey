

I wanted a simple selfhosted pastebin.

* `POST` - Upload content that's in the request body
* `GET` - Download content at the given endpoint

The route corresponds to where the file contents are located.

Example:
```
POST /foo
    This is the content of the POST body

GET /foo - Returns `This is the content of the POST body`
```