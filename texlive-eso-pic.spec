Name:		texlive-eso-pic
Version:	67001
Release:	1
Summary:	Add picture commands (or backgrounds) to every page
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eso-pic
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eso-pic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eso-pic.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eso-pic.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package adds one or more user commands to LaTeX's shipout
routine, which may be used to place the output at fixed
positions. The grid option may be used to find the correct
places.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/eso-pic
%doc %{_texmfdistdir}/doc/latex/eso-pic
#- source
%doc %{_texmfdistdir}/source/latex/eso-pic

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
