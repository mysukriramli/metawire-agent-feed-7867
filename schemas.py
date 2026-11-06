from datetime import timezone as dt_timezone
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

def _get_utc_now_str() -> str:
    """Returns current UTC timestamp in ISO-8601 format."""
    return datetime.now(dt_timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

class HealthResponse(BaseModel):
    """Health check response schema."""
    status: str = Field(default='healthy', description='Service operational health status')
    timestamp: str = Field(default_factory=_get_utc_now_str, description='UTC timestamp of response')

class ToolItem(BaseModel):
    """Individual MCP/Agent tool metadata definition."""
    name: str = Field(default='', description='Tool identifier name')
    description: str = Field(default='', description='Tool functional description')
    input_schema: Dict[str, Any] = Field(default_factory=dict, description='JSON Schema for inputs')

class ToolsResponse(BaseModel):
    """Catalog of all exposed autonomous agent tools."""
    tools: List[Dict[str, Any]] = Field(default_factory=list, description='List of available tools and schemas')

class ExplainabilityWeights(BaseModel):
    """Weights applied to core indices for impact scoring."""
    emergence: float = Field(default=0.3, description='Emergence Index weight')
    momentum: float = Field(default=0.25, description='Reality Momentum Index weight')
    adoption: float = Field(default=0.2, description='Cross-Domain Influence weight')
    capital: float = Field(default=0.15, description='Capital Attention Index weight')
    research: float = Field(default=0.05, description='Research Adoption Index weight')

class ExplainabilityDetail(BaseModel):
    """Explainability breakdown for computed signals."""
    primary_driver: str = Field(default='cross_domain_acceleration', description='Primary driving factor')
    weights: ExplainabilityWeights = Field(default_factory=ExplainabilityWeights, description='Mathematical component weights')

class ComputeEmergingRealityRequest(BaseModel):
    """Input request parameters for `compute_emerging_reality_signal`."""
    target_identifier: str = Field(default='artificial_general_intelligence', description='Target topic, technology, or concept')
    query_parameter: str = Field(default='topic', description='Classification query category')
    lat: float = Field(default=0.0, description='Latitude coordinate [-90, 90]')
    lon: float = Field(default=0.0, description='Longitude coordinate [-180, 180]')
    window_steps: int = Field(default=10, description='Temporal window steps [1, 1000]')

class ComputeEmergingRealityResponse(BaseModel):
    """Output response schema for `compute_emerging_reality_signal`."""
    timestamp: str = Field(default_factory=_get_utc_now_str, description='Analysis UTC timestamp')
    status: str = Field(default='healthy', description='Computation pipeline status')
    primary_metric: float = Field(default=91.7, description='Normalized primary impact score [0-100]')
    secondary_score: float = Field(default=0.94, description='Secondary cross-domain correlation score [0.0-1.0]')
    state_index: float = Field(default=86.2, description='Emergence State Index [0-100]')
    classification: str = Field(default='TRANSFORMATIVE', description='Signal state classification')
    explainability: ExplainabilityDetail = Field(default_factory=ExplainabilityDetail, description='Transparent mathematical decomposition of the signal score')

class SpatialH3TensorRequest(BaseModel):
    """Input request parameters for `get_spatial_h3_tensor`."""
    lat: float = Field(default=2.0442, description='Latitude coordinate [-90, 90]')
    lon: float = Field(default=102.5689, description='Longitude coordinate [-180, 180]')
    resolution: int = Field(default=8, description='Uber H3 spatial resolution [7, 8, 9]')

class SpatialH3TensorResponse(BaseModel):
    """Output response schema for `get_spatial_h3_tensor`."""
    h3_index: str = Field(default='886520d81dfffff', description='Computed 15-character Uber H3 hex index')
    spatial_cell: str = Field(default='886520d81dfffff', description='Target spatial grid cell reference')
    density_score: float = Field(default=64.2, description='Spatial signal density score [0-100]')
    terrain_state_index: float = Field(default=75.1, description='Regional emergence index [0-100]')
    status: str = Field(default='ACTIVE', description='Spatial grid activity state')