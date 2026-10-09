import uuid
from sqlalchemy import Float, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import TimestampMixin


class AuditLog(Base, TimestampMixin):
    __tablename__ = "audit_logs"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    session_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("chat_sessions.id", ondelete="SET NULL"),
        nullable=True,
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="SET NULL"),
        nullable=True,
    )
    approval_ticket_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("approval_tickets.id", ondelete="SET NULL"),
        nullable=True,
    )
    action_type: Mapped[str] = mapped_column(
        String(100),
        index=True,
        nullable=False,
    )
    tool_name: Mapped[str] = mapped_column(
        String(255),
        index=True,
        nullable=True,
    )
    parameters: Mapped[dict] = mapped_column(
        JSONB,
        default=dict,
        nullable=True,
    )
    execution_result: Mapped[dict] = mapped_column(
        JSONB,
        default=dict,
        nullable=True,
    )
    execution_latency_ms: Mapped[float] = mapped_column(
        Float,
        nullable=True,
    )
    status_code: Mapped[str] = mapped_column(
        String(50),
        default="SUCCESS",
        nullable=False,
    )

    # Relationships
    session = relationship("ChatSession", back_populates="audit_logs")
    user = relationship("User", back_populates="audit_logs")
    approval_ticket = relationship("ApprovalTicket", back_populates="audit_logs")
