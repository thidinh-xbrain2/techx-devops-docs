# XBrain DevOps Docs

Tài liệu DevOps để review và để team đọc làm theo. Mỗi doc trả lời: làm gì, làm ở đâu, ai làm, vì sao, kiểm tra thế nào.

## Danh sách doc

| Doc | Nội dung | Trạng thái |
|---|---|---|
| [01 · Cross-tenant access](docs/01-cross-tenant-access.md) | User `@xbrain.com.vn` đăng nhập AWS Landing Zone qua Entra ID của TechX | Chờ review |

## Cấu trúc

```
8-Docs/
├── README.md          danh sách doc
├── docs/              mỗi doc một file NN-ten-kebab.md
├── images/            ảnh chụp màn hình, tên kebab-case
└── templates/         khung doc mới
```

## Quy ước

- Viết ngắn: mỗi bước một dòng, có cột "Vì sao".
- Sơ đồ dùng Mermaid; ảnh chụp chỉ để minh hoạ màn hình.
- Tag: [Confirmed], [Fact] (kèm link), [Assumption], [Recommendation].
- Không ghi mật khẩu, token, SCIM token, account ID thật nếu chưa được phép.
- Câu hỏi chưa chốt để ở mục "Câu hỏi mở" cuối doc.
- Review qua git (commit, PR); sau khi duyệt mới chuyển sang Confluence.
