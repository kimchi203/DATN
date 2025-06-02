import cutecharts.charts as ctc
from datetime import datetime
from chung import *


def repot_html(tong_sotestcase, thanh_cong, that_bai, loi, testsuite, thoi_gian_hien_tai, ketthuc, chenh_lech_thoi_gian,
               browser_version):
    # Tạo biểu đồ tròn
    chart = ctc.Pie("Kết quả chạy test", width='500px', height='400px')

    # Đặt các tùy chọn cho biểu đồ
    chart.set_options(
        labels=['Passed', 'Failed', 'Error'],  # Nhãn cho các phần
        inner_radius=0,   # Bán kính nội đồng
        colors=['#2196F3', '#F44336', '#FFC107']
    )
    thanhcong = thanh_cong
    thatbai = that_bai
    loi = loi
    dathuchien = thanhcong + thatbai + loi
    # Thêm dữ liệu cho biểu đồ
    chart.add_series([thanhcong, thatbai, loi])  # Dữ liệu
    # Tạo dòng chữ với màu sắc tương ứng
    text_content = """
    <p class="custom-img">
        <span style='color: #2f4554;'>Tổng số trường hợp kiểm thử: {}</span>,
        <span style='color: #603F8B;'>Đã thực hiện: {}</span>,
        <span style='color: #2196F3;'>Thành công: {}</span>,
        <span style='color: #F44336;'>Thất bại: {}</span>,
        <span style='color: #FFC107;'>Lỗi: {}</span>
    </p>
    """.format(tong_sotestcase, dathuchien, thanhcong, thatbai, loi)

    # Thời gian bắt đầu chạy và thời gian kết thúc
    text_content_2 = """
    <p class="custom-img">
        
        <span style='color: #2f4554;'>Thời gian bắt đầu: {}</span>,
        <span style='color: #2f4554;'>Thời gian kết thúc: {}</span>
    </p>
    """.format(thoi_gian_hien_tai, ketthuc)
    # Danh sách testcase:
    text = """
    <p class="custom-img">
    <span style='color: #2f4554;'>Danh sách testcase: </span>
    </p>
    """
    # Chi tiết
    text_chitiet = """
        <p class="custom-img">
        <span style='color: #2f4554;'>Chi tiết: </span>
        </p>
        """
    # Tạo bảng HTML
    table_content = """
    <table border='1' style='margin-right: 50px;'>
        <tr>
            <th colspan="2" style="text-align: center;">Thứ tự</th>
            <th style="text-align: center;">Tên Testcase</th>
            <th colspan="2" style="text-align: center;">Trạng Thái</th>
            <th style="text-align: center;">Chi tiết</th>
        </tr>
    """
    ct = ''
    color = ''
    detail_divs = ''
    test_case_failed = False
    for i, testcase in enumerate(testsuite, start=1):
        testcase_status = testcase['status']
        testcase_name = testcase['testcase']

        if testcase_status.lower() == 'fail':
            color = '#0292B7'
        elif testcase_status.lower() == 'err':
            color = '#FFD53D'
        else:
            color = '#2f4554'

        if testcase_status.lower() == 'fail' or testcase_status.lower() == 'err':
            ct = '<a href=' + '#' + testcase_name + '>Chi tiết</a>'
        else:
            ct = ''
        table_content += """
        <tr>
            <td colspan="2" style="text-align: center;color: {};">{}</td>
            <td style="color: {};">{}</td>
            <td colspan="2" style="text-align: center; color: {};">{}</td>
            <td style="text-align: center;">{}</td>
        </tr>
        """.format(color, i, color, testcase_name, color, testcase_status.lower(), ct)
        if testcase_status.lower() == 'fail' or testcase_status.lower() == 'err':
            test_case_failed = True
            testcase_image = upload_image_to_imgbb(api_key, testcase['screenshot'])
            # testcase_image = upload_image_to_imgur(testcase['screenshot'], client_id)
            a_video, shortcode = upload_video(username_stream, password_stream, testcase['video'])
            testcase_video = f"https://streamable.com/e/{shortcode}"
            detail_divs += """
             <div id="{}">
                 <h3>Chi tiết của {} ({})</h3>
                 <p>Nội dung chi tiết của testcase...</p>
                 <div class="img-video-container">
                 <img src="{}" alt="Example Image">
                 <div class="responsive-video-container">
                     <iframe src="{}" frameborder="0" allowfullscreen></iframe>
                </div>
                </div>
             </div>
         """.format(testcase_name, testcase_name, testcase_status, testcase_image, testcase_video)
        # basicfun.DeleteFolder(testcase_name)
        # basicfun.DeleteImageFile(testcase.get_video())
    table_content += "</table>"

    # Lưu biểu đồ vào file HTML
    # html_content = chart.render()+ text_content+text_content_2+text+table_content

    # Lưu biểu đồ vào file HTML
    html_content = f"""
    <div class="container">
        <div class="chart-container">
            {chart.render()}
        </div>
        <div class="content">
            {text_content}
            {text_content_2}
            {text}
            {table_content}
            {text_chitiet if test_case_failed else ''}
            {detail_divs}
        </div>
    </div>
    <!-- Nút Scroll to Top -->
    <button onclick="scrollToTop()" id="scrollToTopBtn" title="Go to top">
    </button>

    <script src="script.js"></script>
    """

    # Thêm CSS để tạo layout
    html_content += """
    <style>
        #scrollToTopBtn {
        display: none; /* Ẩn nút */
        position: fixed; /* Định vị cố định ở một vị trí cụ thể */
        bottom: 20px; /* Cách đáy 20px */
        right: 30px; /* Cách phải 30px */
        z-index: 99; /* Đặt nút lên trên các phần tử khác */
        border: none; /* Không có viền */
        outline: none; /* Không có viền khi nhấn */
        background-color: transparent; /* Nền trong suốt */
        cursor: pointer; /* Con trỏ dạng tay khi di chuột qua */
        padding: 15px; /* Khoảng cách trong */
        border-radius: 10px; /* Bo tròn góc */
        font-size: 18px; /* Kích thước chữ */
        }

        #scrollToTopBtn:hover img {
            background-color: #753647; /* Đổi màu nền khi di chuột qua */
            border-radius: 50%; /* Bo tròn biểu tượng */
        }
        .container {
            display: flex;
            align-items: flex-start;
        }

        .chart-container {
            flex: 0.3;
            margin-right: 20px;
        }

        .content {
            flex: 1;
        }
        table {
                border-collapse: collapse;
                width: 100%;
            }

            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;
            }
            th {
                text-align: center;
                }

            th, td {
                width: auto;
            }

            div[id^="Testcase"] {
                margin-top: 20px;
            }

             .img-video-container {
            width: 100%;
            max-width: 500px;
            margin-top: 10px;
        }

        .img-video-container img {

            width: 100%;
            max-width: 100%;
            height: auto;
            margin-bottom: 10px;
        }

        .responsive-video-container {
            position: relative;
            width: 100%;
            padding-top: 100%;
        }

        .responsive-video-container iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }
    </style>"""
    with open("testcase_report.html", "w", encoding="utf-8") as f:
        f.write(html_content)

