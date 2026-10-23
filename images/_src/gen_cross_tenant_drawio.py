"""Sinh images/cross-tenant-architecture.drawio. Chạy: python images/_src/gen_cross_tenant_drawio.py"""
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / 'cross-tenant-architecture.drawio'
F = 'fontFamily=Helvetica;'
cells = []


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')


def v(id_, value, style, x, y, w, h, parent='1'):
    cells.append(f'<mxCell id="{id_}" value="{esc(value)}" style="{style}" vertex="1" parent="{parent}">'
                 f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/></mxCell>')


def e(id_, src, tgt, label='', dashed=False, extra='', pts=None):
    st = (f'edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;endArrow=block;endFill=1;strokeWidth=2;'
          f'strokeColor=light-dark(#545B64,#D4D4D4);{F}fontSize=11;'
          + ('dashed=1;' if dashed else '') + extra)
    geo = '<mxGeometry relative="1" as="geometry">'
    if pts:
        geo += '<Array as="points">' + ''.join(f'<mxPoint x="{px}" y="{py}"/>' for px, py in pts) + '</Array>'
    geo += '</mxGeometry>'
    cells.append(f'<mxCell id="{id_}" style="{st}" edge="1" parent="1" source="{src}" target="{tgt}">{geo}</mxCell>')
    if label:
        cells.append(f'<mxCell id="{id_}-lbl" value="{esc(label)}" style="edgeLabel;html=1;align=center;verticalAlign=middle;'
                     f'{F}fontSize=11;labelBackgroundColor=light-dark(#FFFFFF,#1E1E1E);" vertex="1" connectable="0" parent="{id_}">'
                     f'<mxGeometry x="0" relative="1" as="geometry"><mxPoint as="offset"/></mxGeometry></mxCell>')


def tenant(id_, label, x, y, w, h, stroke, fill):
    v(id_, label, f'rounded=1;arcSize=2;whiteSpace=wrap;html=1;verticalAlign=top;align=left;spacingLeft=12;spacingTop=6;'
      f'fontStyle=1;fontSize=14;fontColor={stroke};strokeColor={stroke};strokeWidth=2;fillColor=light-dark({fill},{fill});'
      f'fillStyle=auto;container=0;{F}', x, y, w, h)


def node(id_, label, sub, x, y, icon_style, tint, stroke):
    v(id_ + '-box', '', f'fillColor={tint};strokeColor={stroke};rounded=1;whiteSpace=wrap;html=1;container=0;shadow=1;strokeWidth=1.5;{F}',
      x, y, 120, 120)
    v(id_, f'<b>{label}</b><div><i>{sub}</i></div>' if sub else f'<b>{label}</b>',
      icon_style + f'verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontColor=#232F3E;{F}',
      x + 36, y + 22, 48, 48)


def azure(img):
    return f'image;aspect=fixed;html=1;points=[];image=img/lib/azure2/identity/{img}.svg;'


def aws_res(shape, color):
    return (f'sketch=0;outlineConnect=0;fillColor={color};strokeColor=none;dashed=0;aspect=fixed;'
            f'shape=mxgraph.aws4.{shape};')


def aws_svc(res, color):
    return (f'sketch=0;outlineConnect=0;fillColor={color};strokeColor=#ffffff;dashed=0;aspect=fixed;'
            f'shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.{res};')


def badge(n, x, y):
    v(f'step-{n}', str(n), f'rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=default;fontColor=#FFFFFF;fontStyle=1;'
      f'fontSize=16;{F}shadow=1;glass=0;strokeWidth=2;align=center;verticalAlign=middle;labelBackgroundColor=none;', x, y, 28, 28)


# Title
v('title', 'XBrain truy cập AWS Landing Zone của TechX qua Microsoft Entra ID cross-tenant',
  f'text;html=1;align=left;verticalAlign=top;fontSize=28;fontStyle=1;{F}', 40, 24, 1700, 40)
v('subtitle', 'User @xbrain.com.vn được mời vào tenant TechX dưới dạng guest (B2B collaboration), đồng bộ sang IAM Identity Center bằng SCIM và đăng nhập bằng SAML',
  f'text;html=1;align=left;verticalAlign=top;fontSize=15;{F}', 44, 66, 1700, 26)
v('title-sep', '', f'line;strokeWidth=2;html=1;strokeColor=#FF9900;{F}', 44, 96, 1710, 10)

XB, XBF = '#0078D4', '#0078D40D'   # XBrain
TX, TXF = '#5C2D91', '#5C2D910D'   # TechX
tenant('tenant-xbrain', 'Tenant XBrain · xbrain.com.vn', 40, 130, 290, 600, XB, XBF)
tenant('tenant-techx', 'Tenant TechX · techxcorp.com', 380, 130, 700, 600, TX, TXF)
v('aws-cloud', 'AWS Landing Zone của TechX',
  'points=[[0,0],[0.25,0],[0.5,0],[0.75,0],[1,0],[1,0.25],[1,0.5],[1,0.75],[1,1],[0.75,1],[0.5,1],[0.25,1],[0,1],[0,0.75],[0,0.5],[0,0.25]];'
  'outlineConnect=0;gradientColor=none;html=1;whiteSpace=wrap;fontSize=14;fontStyle=1;shape=mxgraph.aws4.group;'
  'grIcon=mxgraph.aws4.group_aws_cloud;strokeColor=#232F3E;fillColor=light-dark(#232F3E0D,#232F3E0D);fillStyle=auto;'
  f'verticalAlign=top;align=left;spacingLeft=30;fontColor=#232F3E;dashed=0;container=0;{F}', 1130, 130, 620, 600)

XT, TT = '#E5F1FB', '#F1EAF8'
# XBrain
node('xb-entra', 'Microsoft Entra ID', 'xác thực tại tenant gốc', 125, 180, azure('Azure_Active_Directory'), XT, XB)
node('xb-user', 'User XBrain', '@xbrain.com.vn', 125, 380, azure('Users'), XT, XB)
node('xb-group', 'Security group', 'người được phép vào AWS', 125, 570, azure('Groups'), XT, XB)
# TechX
node('tx-cta', 'Cross-tenant access', 'Inbound B2B: chỉ group XBrain', 440, 570, azure('External_Identities'), TT, TX)
node('tx-guest', 'Guest user', 'User type = Guest', 440, 380, azure('Users'), TT, TX)
node('tx-group', 'Group trong TechX', 'chứa guest XBrain', 660, 380, azure('Groups'), TT, TX)
node('tx-app', 'Enterprise app', 'AWS IAM Identity Center', 900, 380, azure('Enterprise_Applications'), TT, TX)
# AWS
node('aws-iic', 'IAM Identity Center', 'user, group từ SCIM', 1190, 380, aws_svc('single_sign_on', '#DD344C'), '#FFEBEE', '#DD344C')
node('aws-ps', 'Permission set', 'theo vai trò', 1400, 380, aws_res('permissions', '#DD344C'), '#FFEBEE', '#DD344C')
node('aws-acc', 'AWS account', 'workload của TechX', 1600, 380, aws_res('organizations_account', '#E7157B'), '#FCE4EC', '#E7157B')

# Edges
e('e1', 'xb-user-box', 'xb-group-box', 'member', extra='exitX=0.5;exitY=1;entryX=0.5;entryY=0;')
e('e2', 'xb-group', 'tx-cta', 'được phép')
e('e3', 'xb-user', 'tx-guest', 'được mời')
e('e-cta', 'tx-cta', 'tx-guest-box', 'kiểm soát', dashed=True, extra='exitX=0.5;exitY=0;entryX=0.5;entryY=1;')
e('e5a', 'tx-guest', 'tx-group', 'member')
e('e5b', 'tx-group', 'tx-app', 'assigned')
e('e5c', 'tx-app', 'aws-iic', 'SCIM', extra='exitX=1;exitY=0.35;entryX=0;entryY=0.35;')
e('e-saml', 'tx-app', 'aws-iic', 'SAML', dashed=True, extra='exitX=1;exitY=0.75;entryX=0;entryY=0.75;')
e('e6a', 'aws-iic', 'aws-ps', 'gán')
e('e6b', 'aws-ps', 'aws-acc', 'truy cập')
e('e-auth', 'tx-guest', 'xb-entra', 'chuyển về xác thực', dashed=True, extra='exitX=0.5;exitY=0;entryX=1;entryY=0.5;')

# Badges
badge(1, 205, 520)
badge(2, 240, 570)
badge(3, 240, 350)
badge(4, 990, 340)
badge(5, 590, 340)
badge(6, 1320, 340)

# Legend
LX, LY = 1790, 130
v('legend-bg', '', 'verticalLabelPosition=bottom;verticalAlign=top;html=1;shape=mxgraph.basic.rect;fillColor2=none;strokeWidth=1;size=20;'
  'indent=5;fillColor=light-dark(#EDF3FF,#305363);strokeColor=#6c8ebf;', LX, LY, 520, 600)
steps = [
    ('Tạo security group', 'Tenant XBrain tạo group chứa người cần truy cập AWS.'),
    ('Cho phép tenant XBrain', 'TechX thêm XBrain vào Cross-tenant access settings, chỉ cho phép group ở bước 1, tin MFA của XBrain.'),
    ('Mời guest', 'TechX mời user XBrain; user chấp nhận lời mời và trở thành guest.'),
    ('Cấu hình claim', 'Name ID của guest lấy từ user.mail thay cho UPN dạng #EXT#.'),
    ('Gán và đồng bộ', 'Guest vào group TechX, group được gán vào app; SCIM đồng bộ sang IAM Identity Center.'),
    ('Cấp quyền AWS', 'Gán group với permission set và account; user đăng nhập access portal bằng SAML.'),
]
for i, (t, d) in enumerate(steps, 1):
    y = LY + 30 + (i - 1) * 92
    v(f'lg-{i}-badge', str(i), f'rounded=1;whiteSpace=wrap;html=1;fillColor=#007CBD;strokeColor=default;fontColor=#FFFFFF;fontStyle=1;'
      f'fontSize=20;labelBackgroundColor=none;{F}shadow=1;glass=0;strokeWidth=2;', LX + 20, y, 40, 38)
    v(f'lg-{i}-text', f'<b>{t}</b><div><span style="color: light-dark(rgb(0,0,0), rgb(255,255,255));">{d}</span></div>',
      f'text;html=1;align=left;verticalAlign=top;fontSize=13;whiteSpace=wrap;labelBackgroundColor=none;{F}', LX + 72, y - 2, 430, 80)
v('lg-line', '<b>Đường liền</b>: luồng cấu hình và đồng bộ · <b>Đường đứt</b>: luồng đăng nhập và kiểm soát',
  f'text;html=1;align=left;verticalAlign=top;fontSize=12;whiteSpace=wrap;{F}', LX + 20, LY + 590 - 40, 480, 36)

xml = ('<mxfile host="Electron" version="29.6.1"><diagram name="Cross-tenant" id="cross-tenant">'
       '<mxGraphModel dx="1200" dy="800" grid="0" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="0" '
       'pageScale="1" pageWidth="1100" pageHeight="850" math="0" shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>'
       + ''.join(cells) + '</root></mxGraphModel></diagram></mxfile>')
OUT.write_text(xml, encoding='utf-8')
print(OUT)
