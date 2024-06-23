from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Position
import chess
import chess.svg

class PositionDetailView(DetailView):
  model = Position
  template_name = "base.html"
  context_object_name = "position"

  def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Get svg for current position
        fen = context["position"].fen
        current_board = chess.Board(fen=fen)
        position_image = str(chess.svg.board(current_board, size=400))

        # Add svg to context
        context["image"] = position_image

        return context

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

