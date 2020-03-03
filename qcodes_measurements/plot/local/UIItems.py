from .RemoteProcessWrapper import RPGWrappedBase

class TableWidget(RPGWrappedBase):
    """
    Table
    """
    _base = "TableWidget"

class LegendItem(RPGWrappedBase):
    """
    Legend handling code
    """
    _base = "LegendItem"

class TextItem(RPGWrappedBase):
    _base = "DraggableTextItem"
    _ANCHORS = {'tl': (0,0),
                'tr': (1,0),
                'bl': (0,1),
                'br': (1,1)}

    def setParentItem(self, p):
        self._base_inst.setParentItem(p)
        if isinstance(p, RPGWrappedBase):
            p._items.append(self)

    def anchor(self, anchor):
        """
        Put this text box in a position relative to
        (tl, tr, bl, br)
        """
        anchor_point = TextItem._ANCHORS[anchor]
        self._base_inst.anchor(itemPos=anchor_point,
                               parentPos=anchor_point,
                               offset=(0,0))

    @property
    def offset(self):
        return self.getOffset()
    @offset.setter
    def offset(self, offs):
        if not isinstance(offs, tuple) or len(offs) != 2:
            raise ValueError("Must be a tuple (x, y)")
        self.setOffset(offs)

    @property
    def text(self):
        text = "".join(self.getText()).replace("<br>", "\n")
        return text
    @text.setter
    def text(self, text):
        # Replace new lines with HTML line breaks
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")
        text = text.replace("\n", "<br>")
        self.setText(str(text))

class PlotAxis(RPGWrappedBase):
    _base = "AxisItem"

    @property
    def label(self):
        return self.labelText
    @label.setter
    def label(self, text):
        self.setLabel(text=text)

    @property
    def units(self):
        return self.labelUnits
    @units.setter
    def units(self, units):
        self.setLabel(units=units)

    @property
    def unit(self):
        return self.labelUnits
    @unit.setter
    def unit(self, units):
        self.setLabel(units=units)
