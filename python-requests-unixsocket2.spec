%define module requests_unixsocket2
%define oname requests_unixsocket

# NOTE This is a maintained fork of python-requests-unixsocket -
# NOTE https://github.com/msabramo/requests-unixsocket
# NOTE which should be a drop-in replacement.
# NOTE See this issue for more info:
# NOTE https://github.com/msabramo/requests-unixsocket/issues/73#issuecomment-2125848213

Name:		python-requests-unixsocket2
Version:	1.0.1
Release:	1
Summary:	Use requests to talk HTTP via a UNIX domain socket
License:	ISC
Group:		Development/Python
URL:		https://gitlab.com/thelabnyc/requests-unixsocket2
Source0:	%{URL}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(wheel)

# Obsolete the old unmaintaned package and provide upgrade path
%rename	python-requests-unixsocket
Provides:	python%{pyver}dist(requests-unixsocket) = %{EVRD}

%description
Use requests to talk HTTP via a UNIX domain socket.

%prep -a
# Remove shebang from tests script
sed -i '1d' requests_unixsocket/tests/test_requests_unixsocket.py

%files
%doc README.md
%{python_sitelib}/%{oname}
%{python_sitelib}/%{module}-%{version}.dist-info
