# TechX DevOps Docs

Tài liệu DevOps để review và để team đọc làm theo. Mỗi doc trả lời: làm gì, làm ở đâu, ai làm, vì sao, kiểm tra thế nào.

## Danh sách doc

| Doc | Nội dung |
|---|---|
| [01 · Cross-tenant access](docs/01-cross-tenant-access.md) | User `@xbrain.com.vn` đăng nhập AWS Landing Zone qua Entra ID của TechX |

## Cấu trúc

```
8-Docs/
├── README.md          danh sách doc
├── docs/              mỗi doc một file NN-ten-kebab.md
├── images/            ảnh chụp màn hình, tên kebab-case
└── templates/         khung doc mới
```

## Quy ước

- Văn phong AWS docs: mở bài, Cách hoạt động, Điều kiện tiên quyết, Bước N với thủ tục "Để …", Xử lý sự cố, Bước tiếp theo. Mẫu: doc 01.
- Sơ đồ dùng Mermaid; ảnh chụp chỉ để minh hoạ màn hình.
- Tag: [Confirmed], [Fact] (kèm link), [Assumption], [Recommendation].
- Không ghi mật khẩu, token, SCIM token, account ID thật nếu chưa được phép.
- Doc chỉ ghi nội dung đã chốt. Không ghi dòng người soạn hay trạng thái, không để mục "chờ bổ sung" hay câu hỏi mở; câu hỏi chưa chốt trao đổi riêng.
- Review qua git (commit, PR); sau khi duyệt mới chuyển sang Confluence.
