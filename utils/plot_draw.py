from PIL import Image, ImageDraw, ImageFont
import os


class PlotDraw:
    """
    This class is responsible for drawing the image and saving it
    as an image file.
    """
    path = ''
    size = ()
    draw_object = {}

    def __init__(self, fp, size):
        self.path = fp
        self.size = size

    def set_draw_object(self, do):
        """
        Sets the coordinates for plotting the actual line.
        :param actual: List of tuples (x, y)
        :return:
        """
        self.draw_object = do

    def draw_image(self):
        img = Image.new('RGB', self.size, color='white')

        # Set the font
        cwd = os.getcwd()
        font_location = os.path.join(cwd, 'res', 'fonts', 'Nonserif.ttf')
        fnt = ImageFont.truetype(font_location, 16)
        fnt_axes = ImageFont.truetype(font_location, 14)

        draw = ImageDraw.Draw(img)

        projected = self.draw_object['projected']
        draw.line(projected, fill='blue', width=2)

        actual = self.draw_object['actual']
        draw.line(actual, fill='red', width=2)

        hor_grid_lines = self.draw_object['hor_grid_lines']
        for hl in hor_grid_lines:
            draw.line(hl, fill='gray', width=1)

        vert_axis_labels = self.draw_object['vert_axis_label']
        for val in vert_axis_labels:
            draw.text(val['location'], str(val['text']), fill=0, font=fnt_axes)

        border_lines = self.draw_object['border_lines']
        for bl in border_lines:
            draw.line(bl, fill='black', width=2)

        vert_grid_lines = self.draw_object['vert_grid_lines']
        for vl in vert_grid_lines:
            draw.line(vl, fill='gray', width=1)

        hor_axis_labels = self.draw_object['hor_axis_label']
        for hal in hor_axis_labels:
            draw.text(hal['location'], str(hal['text']), fill=0, font=fnt_axes)

        legend_object = self.draw_object['legend']

        legend_projected = legend_object['line_projected']
        legend_projected_line = legend_projected['line']
        legend_projected_label = legend_projected['label']
        draw.line(legend_projected_line, fill='blue', width=2)
        draw.text(legend_projected_label['location'],
                  legend_projected_label['text'], fill='blue', font=fnt, anchor=-10)

        legend_projected = legend_object['line_actual']
        legend_projected_line = legend_projected['line']
        legend_projected_label = legend_projected['label']
        draw.line(legend_projected_line, fill='red', width=2)
        draw.text(legend_projected_label['location'],
                  legend_projected_label['text'], fill='red', font=fnt, anchor=-10)

        img.save(self.path, quality=100)
        img.resize((self.size[0]*2, self.size[1]*2), Image.ANTIALIAS)
        img.close()
